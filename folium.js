map_8e867c089ae348865072dac49e6862d7.on('zoomend', function() {                        //triggers after zoom event
        if (map_8e867c089ae348865072dac49e6862d7.getZoom() <11){                        //where x is the zoom level where the change occurs
                let zz = document.querySelectorAll('.samba');
                for (var xu = 0; xu < zz.length; xu++){
                        //els[x].style.display = 'none';
                        zz[xu].style.display = 'block';
        }}
        else {
            let xxy = document.querySelectorAll('.samba');
                for (var t = 0; t < xxy.length; t++){
                        //els[x].style.display = 'none';
                        xxy[t].style.display = 'none';
        }
    }});       



    map_e55d70d31368bee9c056a0da32ba15ca.on('zoomend',function() {                        //triggers after zoom event
        if (map_e55d70d31368bee9c056a0da32ba15ca.getZoom() >11){                        //where x is the zoom level where the change occurs
                let zz = document.querySelectorAll('.pin');
                for (var xu = 0; xu < zz.length; xu++){
                        zz[xu].style.display = 'none';}
                let xxp = document.querySelectorAll('.api');
                for (var t = 0; t < xxp.length; t++){
                        xxp[t].style.display = 'block';
        }}
        else {
            let xxy = document.querySelectorAll('.pin');
                for (var t = 0; t < xxy.length; t++){
                        xxy[t].style.display = 'block';}

            let xxz = document.querySelectorAll('.api');
                for (var t = 0; t < xxz.length; t++){

                        xxz[t].style.display = 'none';
        }
    }});   
