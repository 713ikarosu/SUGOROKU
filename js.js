
//すごろく
var num; //サイコロの目の値
var marg = 30; //残りのマス数(差)
var sum;

(function () {
  "use strict";

//サイコロ
    document.getElementById('saikoro').addEventListener('click', function () {
      $(function(){
        $('ul li').each(function(){
            $(this).css({opacity: '1.0'});
        })
      });

      var Values = ['1', '2', '3', '4', '5', '6'];
      var saikoroValue = Math.floor(Math.random() * Values.length);
      document.getElementById('square').innerHTML = Values[saikoroValue];

      num = Values[saikoroValue]; //変数 <- 文字列
      Number(num); //値に
      marg = marg - num;

      document.getElementById('now').innerHTML = marg;
  //サイコロ終わり

      sum = 30 - marg;
      var order = 'nth-child('+ sum +')';

      $(function(){
        $('ul li:' + order).each(function(){
            $(this).css({opacity: '0.5'});
        })
      });


//ゴール判定
    if (marg <= 0) {
      alert("ゴール！");
	    window.location.reload();
    };
  });
})();
