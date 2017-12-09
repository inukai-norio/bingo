var dataset = document.currentScript.dataset;

$(function () {
  var roulette = $('#js-roulette');
  var staffId = $('#js-staff-id');
  var staffName = $('#js-staff-name');
  var start = $('#js-roulette-start');
  var stop = undefined;
  var next = $('#js-next-page');

  var showStaffInfo = function (id, name) {
    id.show();
    name.show();
  };

  var option = {
    speed: 50,
    duration: 4,
    stopImageNumber: dataset.imgNumber,

    // ルーレット回転開始
    startCallback: function() {
      start.hide();
      console.log('start');
    },

    // ルーレット減速開始
    slowDownCallback: function() {
      console.log('slowDown');
    },

    // ルーレット停止
    stopCallback: function($stopElm) {
      console.log('stop');

      showStaffInfo(staffId, staffName);
      next.show();
    }
  }

  // Init!
  roulette.roulette(option);

  // START!
  start.click(function(){
    roulette.roulette('start');
  });

  // STOP!
  stop.click(function(){
    roulette.roulette('stop');
  });

  // Go to next page
  next.click(function() {
    console.log('Next clicked');
  })
});

