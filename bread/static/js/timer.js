//<script language="javascript">

$(document).ready(function(){
    //초기값
    var hour = {{ bread.release_at.hour }};
    var minute = {{ bread.release_at.min }};
    var second = 0;
    
    // 초기화
    $(".countTimeHour").html(hour);
    $(".countTimeMinute").html(minute);
    $(".countTimeSecond").html(second);
    
    var timer = setInterval(function () {
            // 설정
            $(".countTimeHour").html(hour);
            $(".countTimeMinute").html(minute);
            $(".countTimeSecond").html(second);
            
            if(second == 0 && minute == 0 && hour == 0){
                alert('타이머 종료.');
                clearInterval(timer); /* 타이머 종료 */
            }else{
                second--;
                
                // 분처리
                if(second < 0){
                    minute--;
                    second = 59;
                }
                
                //시간처리
                if(minute < 0){
                    if(hour > 0){
                        hour--;
                        minute = 59;
                    }
                    
                }
            }
        }, 1000); /* millisecond 단위의 인터벌 */
});


//</script>