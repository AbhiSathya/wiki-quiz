const API_BASE = "http://localhost:8000";

export async function generateQuiz(url: string) {
  const res = await fetch(`${API_BASE}/quiz/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url })
  });

  if (!res.ok) {
    throw new Error("Failed to generate quiz");
  }

  return res.json();
}

export async function fetchHistory() {
  const res = await fetch(`${API_BASE}/history`);
  return res.json();
}

export async function fetchQuizById(id: number) {
  const res = await fetch(`${API_BASE}/quiz/${id}`);
  return res.json();
}

export async function previewArticle(url: string) {
  const res = await fetch(
    `${API_BASE}/quiz/preview?url=${encodeURIComponent(url)}`
  );

  if (!res.ok) {
    throw new Error("Invalid URL");
  }

  return res.json(); // { title }
}
