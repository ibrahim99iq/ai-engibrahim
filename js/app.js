function loadReport(){

    const dateValue=document.getElementById("reportDate").value;
    const message=document.getElementById("message");
    const frame=document.getElementById("reportFrame");

    message.innerText="";
    frame.src="";

    if(!dateValue){
        message.innerText="يرجى اختيار تاريخ أولاً";
        return;
    }

    const filePath="history_images/"+dateValue+".pdf";

    fetch(filePath,{method:"HEAD"})
    .then(response=>{
        if(response.ok){
            frame.src=filePath;
        }else{
            message.innerText="لا يوجد تقرير لهذا التاريخ";
        }
    })
    .catch(()=>{
        message.innerText="لا يوجد تقرير لهذا التاريخ";
    });

}

function openInNewTab(){

    const dateValue=document.getElementById("reportDate").value;

    if(!dateValue){
        alert("اختر تاريخ أولاً");
        return;
    }

    const filePath="history_images/"+dateValue+".pdf";
    window.open(filePath,"_blank");

}