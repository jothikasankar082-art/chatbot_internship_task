function addMessage(message, sender){

    const chatBox = document.getElementById("chat-box");

    const div = document.createElement("div");

    div.className = sender === "user" ? "user-message" : "bot-message";

    div.innerHTML = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

}

function sendMessage(){

    const input = document.getElementById("user-input");

    const message = input.value.trim();

    if(message==="") return;

    addMessage(message,"user");

    fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            message:message

        })

    })

    .then(res=>res.json())

    .then(data=>{

        addMessage(data.response,"bot");

    });

    input.value="";

}

document.getElementById("user-input")

.addEventListener("keypress",function(e){

    if(e.key==="Enter"){

        sendMessage();

    }

});