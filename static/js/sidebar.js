
    var sidebar = document.getElementById("sidebar");
    var menu= document.getElementById("menu");
    var back=document.getElementById("back");  


    menu.addEventListener('click',()=>{
        if(sidebar.style.visibility==='hidden'){
            sidebar.style.visibility='visible';
            
        }else{
            sidebar.style.visibility='hidden';
        }
    })


    back.addEventListener('click',()=>{
        if(sidebar.style.visibility==='visible'){
            sidebar.style.visibility='hidden';
        }else{
            sidebar.style.visibility='visible';
        }
    })