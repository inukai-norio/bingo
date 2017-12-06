import sqlite3
import os
import random
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)
db_name = './bingo.sqlite3'
img = {
    # ファイル名: 名前
    'A01': '001',
    'A02': '002',
    'A03': '003',
    'A04': '004',
    'A05': '005',
    'A06': '006',
    'A07': '007',
    'B01': '008',
    'B02': '009',
    'B03': '010',
    'B04': '011',
    'B05': '012',
    'B06': '013',
    'B07': '014',
    'C01': '015',
    'C02': '016',
    'C03': '017',
    'C04': '018',
    'C05': '019',
    'C06': '020',
    'C07': '021',
}


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def index():
    return render_template('top.html')


@app.route('/t/<int:content_id>')
def t(content_id):
    if content_id >= len(img):
        return redirect(url_for('t', content_id=content_id % len(img)))

    conn = sqlite3.connect(db_name)

    conn.row_factory = dict_factory
    c = conn.cursor()
    sql_stmt = '''
        SELECT imgid
             , imgkey
          FROM img
         WHERE imgid = ?
    '''
    for row in c.execute(sql_stmt, [content_id]):
        dict_data = row
    dict_data['name'] = img[dict_data['imgkey']]
    file_list = []
    while len(file_list) == 0:
        file_list = random.sample(list(img.keys()), 4)
        if dict_data['imgkey'] in file_list:
            file_list = []
        else:
            file_list.append(dict_data['imgkey'])
            random.shuffle(file_list)
    for i in range(5):
        if file_list[i] == dict_data['imgkey']:
            fileno = i
            break
    filename_list = []
    for one_file in file_list:
        filename = 'img/' + one_file + '.png'
        filename_list.append(url_for('static', filename=filename))
    dict_data['file'] = filename_list
    dict_data['fileno'] = fileno
    dict_data['next'] = dict_data['imgid'] + 1
    app.logger.debug(dict_data)

    return render_template('bingo.html', dict_data=dict_data)


@app.errorhandler(404)
def error_handler(error):
    e = {
        'code': error.code,
        'name': error.name,
        'description': error.description
    }
    e['message'] = '見つかりません。アドレスが間違っていると思われます。'
    return render_template('error.html', error=e), error.code


if __name__ == '__main__':
    if not os.path.exists(db_name):
        conn = sqlite3.connect(db_name)

        conn.row_factory = dict_factory
        c = conn.cursor()
        sql_stmt = '''
            CREATE TABLE img (
                imgid integer,
                imgkey char(3)
            );
        '''
        c.execute(sql_stmt)

        img_s = list(img.keys())
        random.shuffle(img_s)
        purchases = []
        for i in range(len(img_s)):
            purchases.append((i, img_s[i]))
        c.executemany('INSERT INTO img VALUES (?,?)', purchases)

        conn.commit()
    app.run(debug=True)
