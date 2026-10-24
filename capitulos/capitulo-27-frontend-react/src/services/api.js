const API_URL = "http://localhost:8000";

export async function login(email, senha) {
  const resposta = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ username: email, password: senha }),
  });
  if (!resposta.ok) {
    throw new Error("Credenciais inválidas");
  }
  return resposta.json(); // { access_token, token_type }
}

export async function perguntarAoAgente(pergunta, token) {
  const resposta = await fetch(`${API_URL}/chat/agente`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ pergunta }),
  });
  if (!resposta.ok) {
    throw new Error(`Erro ${resposta.status} ao consultar o assistente`);
  }
  return resposta.json(); // { resposta, fonte, ... }
}
