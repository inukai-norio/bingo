var dataset = document.currentScript.dataset;

$(function () {
  var roulette = $('#js-roulette');
  var staffId = $('#js-staff-id');
  var staffName = $('#js-staff-name');
  var next = $('#js-next-page');
  var drumRoll = $('#js-drum-roll')[0];
  var cymbal = $('#js-cymbal')[0];

  var showStaffInfo = function (id, name) {
    id.show();
    name.show();
  };

  var option = {
    speed: 100,
    duration: 0.3,
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
      next.focus();
    }
  }

  // Init!
  roulette.roulette(option);

  // Start
  roulette.roulette('start');

  // Go to next page
  next.click(function() {
    console.log('Next clicked');
  });
});

