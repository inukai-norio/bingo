var dataset = document.currentScript.dataset;

$(function () {
  var roulette = $('#js-roulette');
  var staffId = $('#js-staff-id');
  var staffName = $('#js-staff-name');
  var start = $('#js-roulette-start');
  var stop = undefined;

  $(start).width($(start).height());

  var showStaffInfo = function (id, name) {
    id.show();
    name.show();
  };

  var option = {
    speed : 50,
    duration : 4,
    stopImageNumber : dataset.imgNumber,

    startCallback : function() {
      console.log('start');
    },

    slowDownCallback : function() {
      console.log('slowDown');
    },

    stopCallback : function($stopElm) {
      console.log('stop');

      showStaffInfo(staffId, staffName);
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
});

