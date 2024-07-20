document.addEventListener('DOMContentLoaded', (event) => {

    const chatbot = document.getElementById('chatbot');
    const chatbotIcon = document.getElementById('chatbot-icon-container')
    const closeBtn = document.getElementById('close-btn');
    const chatbox = document.getElementById('chatbox');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');
    const suggestionsContainer = document.getElementById('suggestions');


    // Close button functionality
    closeBtn.addEventListener('click', () => {
        chatbot.style.display = 'none';
        chatbotIcon.style.display = 'block'
    });
    
    // Chatbot Icon functionality
    chatbotIcon.addEventListener('click', () => {
        chatbot.style.display = 'block';
        chatbotIcon.style.display = 'none'
    });

    // Fetch and display question suggestions
    function fetchSuggestions() {
        fetch('/get_suggestions')
            .then(response => response.json())
            .then(data => {
                suggestionsContainer.innerHTML = '';
                data.forEach(question => {
                    const span = document.createElement('span');
                    span.textContent = question;
                    span.addEventListener('click', () => {
                        sendMessage(question);
                    });
                    suggestionsContainer.appendChild(span);
                });
            });
    }

    // Send message functionality
    function sendMessage(text = null) {
        const userText = text || userInput.value.trim();
        if (userText === '') return;
        userInput.value = '';

        const userMessage = document.createElement('p');
        userMessage.classList.add('user-message');
        userMessage.innerHTML = `<b>You:</b> ${userText}`;
        chatbox.appendChild(userMessage);

        fetch(`/get?msg=${userText}`)
            .then(response => response.text())
            .then(data => {
                const botMessage = document.createElement('p');
                botMessage.classList.add('bot-message');
                botMessage.innerHTML = `<b>Bot:</b> ${data}`;
                chatbox.appendChild(botMessage);
                chatbox.scrollTop = chatbox.scrollHeight;
            });
            
        // for new suggestions after every conversation
        fetchSuggestions();
    }

    // Fetch suggestions initially
    fetchSuggestions();

    // Send message on button click or Enter key press
    sendButton.addEventListener('click', () => sendMessage());
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

});
