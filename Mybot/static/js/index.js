
$(document).ready(function() {
    $("#sendButton").click(function() {
        let userInput = $("#userInput").val().trim();
        if (userInput === "") return;

        let chatbox = $("#chatbox");

        // ✅ User message show karein
        chatbox.append("<p><strong>You:</strong> " + userInput + "</p>");

        // ✅ AJAX Request with Render URL
        $.ajax({
            url: "https://mentalhealthchatbot-u414.onrender.com/get_response/", // ✅ Correct Render API URL
            type: "GET",
            data: { query: userInput },
            dataType: "json",
            success: function(response) {
                chatbox.append("<p><strong>Bot:</strong> " + response.reply + "</p>");
                chatbox.scrollTop(chatbox[0].scrollHeight); // ✅ Auto-scroll down
            },
            error: function(xhr, status, error) {
                chatbox.append("<p><strong>Bot:</strong> ❌ Error fetching response!</p>");
                console.error("Error:", error);
            }
        });

        $("#userInput").val(""); // ✅ Clear input field
    });

    // ✅ Enter key support
    $("#userInput").keypress(function(event) {
        if (event.which === 13) { // 13 = Enter key
            $("#sendButton").click();
        }
    });
});
