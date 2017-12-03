import sqlite3
import os
from random import shuffle
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)
db_name = './bingo.sqlite3'
img = {
    # ファイル名: 名前
    '001': '001',
    '002': '002',
    '003': '003',
    '004': '004',
    '005': '005',
    '006': '006',
    '007': '007',
    '008': '008',
    '009': '009',
    '010': '010',
    '011': '011',
    '012': '012',
    '013': '013',
    '014': '014',
    '015': '015',
    '016': '016',
    '017': '017',
    '018': '018',
    '019': '019',
    '020': '020',
    '021': '021',
    '022': '022',
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
    filename = 'img/' + dict_data['imgkey'] + '.png'
    dict_data['file'] = url_for('static', filename=filename)
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
        shuffle(img_s)
        purchases = []
        for i in range(len(img_s)):
            purchases.append((i, img_s[i]))
        c.executemany('INSERT INTO img VALUES (?,?)', purchases)

        conn.commit()
    app.run(debug=True)
