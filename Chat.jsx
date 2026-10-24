import { useState } from "react";
import { perguntarAoAgente } from "../services/api";

export default function Chat({ token }) {
  const [pergunta, setPergunta] = useState("");
  const [mensagens, setMensagens] = useState([]);
  const [carregando, setCarregando] = useState(false);

  async function enviar() {
    if (!pergunta.trim()) return;
    const perguntaAtual = pergunta;
    setMensagens((atual) => [...atual, { autor: "usuario", texto: perguntaAtual }]);
    setPergunta("");
    setCarregando(true);

    try {
      const dados = await perguntarAoAgente(perguntaAtual, token);
      setMensagens((atual) => [
        ...atual,
        { autor: "assistente", texto: dados.resposta, fonte: dados.fonte },
      ]);
    } catch (e) {
      setMensagens((atual) => [...atual, { autor: "assistente", texto: `Erro: ${e.message}` }]);
    } finally {
      setCarregando(false);
    }
  }

  return (
    <div style={{ maxWidth: 600, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h2>Assistente Corporativo</h2>
      <div style={{ minHeight: 300, border: "1px solid #ddd", padding: 12, marginBottom: 12 }}>
        {mensagens.map((m, i) => (
          <div key={i} style={{ textAlign: m.autor === "usuario" ? "right" : "left", marginBottom: 8 }}>
            <p style={{ display: "inline-block", background: "#f0f0f0", padding: "6px 10px", borderRadius: 6 }}>
              {m.texto}
            </p>
            {m.fonte && <div style={{ fontSize: 11, color: "#888" }}>fonte: {m.fonte}</div>}
          </div>
        ))}
        {carregando && <p style={{ color: "#888" }}>Pensando...</p>}
      </div>
      <div style={{ display: "flex", gap: 8 }}>
        <input
          value={pergunta}
          onChange={(e) => setPergunta(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && enviar()}
          placeholder="Digite sua pergunta..."
          style={{ flex: 1, padding: 8 }}
        />
        <button onClick={enviar} disabled={carregando}>Enviar</button>
      </div>
    </div>
  );
}
