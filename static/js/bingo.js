var dataset = document.currentScript.dataset;

$(function () {
  var roulette = $('#js-roulette');
  var staffId = $('#js-staff-id');
  var staffName = $('#js-staff-name');
  var cover = $('#js-app-cover');
  var next = $('#js-next-page');
  var drumRoll = $('#js-drum-roll')[0];
  var cymbal = $('#js-cymbal')[0];

  var showStaffInfo = function (id, name) {
    id.show();
    name.show();
  };

  var option = {
    speed: 50,
    duration: 6,
    stopImageNumber: dataset.imgNumber,

    // ルーレット回転開始
    startCallback: function() {
      drumRoll.play();
    },

    // ルーレット減速開始
    slowDownCallback: function() {
    },

    // ルーレット停止
    stopCallback: function ($stopElm) {
      drumRoll.pause();
      cymbal.play();
      showStaffInfo(staffId, staffName);
      next.show();
    }
  }

  // Init!
  roulette.roulette(option);

  // Start & Stop
  cover.state = 'initial';
  cover.click(function(){
    switch (cover.state) {
      case 'initial':
        cover.removeClass('-initial');
        cover.addClass('-invisible');
        cover.addClass('-reactive');
        cover.state = 'invisible';
        roulette.roulette('start');
        break;

      case 'invisible':
        cover.removeClass('-reactive');
        roulette.roulette('stop');
        break;
    }
  });

  // Go to next page
  next.click(function() {
    console.log('Next clicked');
  });
});

