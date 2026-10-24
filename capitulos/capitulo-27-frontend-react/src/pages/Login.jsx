import { useState } from "react";
import { login } from "../services/api";

export default function Login({ aoLogar }) {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [erro, setErro] = useState(null);

  async function handleSubmit(evento) {
    evento.preventDefault();
    setErro(null);
    try {
      const dados = await login(email, senha);
      aoLogar(dados.access_token);
    } catch (e) {
      setErro(e.message);
    }
  }

  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: 320, margin: "80px auto" }}>
      <h2>Assistente Corporativo</h2>
      <input
        type="email"
        placeholder="E-mail"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        style={{ display: "block", width: "100%", marginBottom: 8 }}
      />
      <input
        type="password"
        placeholder="Senha"
        value={senha}
        onChange={(e) => setSenha(e.target.value)}
        style={{ display: "block", width: "100%", marginBottom: 8 }}
      />
      {erro && <p style={{ color: "red" }}>{erro}</p>}
      <button type="submit">Entrar</button>
    </form>
  );
}
