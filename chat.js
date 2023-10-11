document.addEventListener("DOMContentLoaded", function() {
    const chatMessages = document.getElementById("chat-messages");
    const userMessageInput = document.getElementById("user-message");
    const sendButton = document.getElementById("send-button");
    
    // Toda vez que pressionarmos Enter, uma mensagem será enviada
    userMessageInput.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            sendButton.click();
        }
    });

    sendButton.addEventListener("click", function() {
        const userMessage = userMessageInput.value;
        if (userMessage.trim() === "") return;

        // Aqui será exibida a mensagem do usuário
        displayMessage("Você: " + userMessage);

        // Lógica da Minerva que poderá ser alterada conforme evolução
        const minervaResponse = "Minerva: Olá! Como posso ajudar?";

        displayMessage(minervaResponse);

        // Limpa o campo de entrada
        userMessageInput.value = "";
    });

    function displayMessage(message) {
        const messageElement = document.createElement("p");
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
