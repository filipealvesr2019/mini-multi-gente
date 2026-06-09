// agent.js

// Estado do agente
const agentState = {
    workspace: {}, // arquivos e pastas carregados
    history: [],   // histórico de comandos e respostas
};

// Função principal para processar prompt
async function processPrompt(promptText) {
    // Exemplo: simples eco + logging
    console.log("Prompt recebido:", promptText);

    // Guardar no histórico
    agentState.history.push({ prompt: promptText, response: null });

    // Simulação de resposta
    const responseText = `Comando processado: "${promptText}"`;
    
    // Atualizar histórico
    agentState.history[agentState.history.length - 1].response = responseText;

    // Retornar resposta
    return responseText;
}

// Função para integrar com a UI
export async function handlePromptFromUI(promptText, chatMessagesEl) {
    const response = await processPrompt(promptText);

    // Renderizar no chat
    const msg = document.createElement("div");
    msg.className = "message";
    msg.innerHTML = `
        <div class="message-header"><span>Agente</span><button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.nextElementSibling.innerText)">Copiar</button></div>
        <div class="message-content">${response}</div>
    `;
    chatMessagesEl.appendChild(msg);
    chatMessagesEl.scrollTop = chatMessagesEl.scrollHeight;
}