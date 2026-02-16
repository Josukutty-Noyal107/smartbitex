
import { GoogleGenerativeAI } from "@google/generative-ai";

const MODEL_NAME = 'gemini-1.5-flash';

export async function fetchFoodInfo(foodItem) {
  const apiKey = "AIzaSyBR8p1Jf1cCFmTCna-x-k1ZetFoutHPVuc";
  if (!apiKey) {
    throw new Error("API Key is missing. Please ensure process.env.API_KEY is configured.");
  }

  const ai = new GoogleGenerativeAI({ apiKey });
  
  const systemInstruction = `
    You are an AI Food Assistant. Your goal is to provide short, clear, and actionable food information. When the user gives a food item name, respond using the EXACT structure below. Follow ALL formatting rules strictly.
    FORMAT RULES:
    - Output must be in clean Markdown.
    - Use bold headers exactly as shown.
    - Keep tone helpful and minimalist.
    - Do NOT add extra sections.
    - Do NOT add emojis.
    - Do NOT add explanations outside the structure.
    - Always provide exactly two YouTube search links.
    STRUCTURE:
    **Description:** Write 1–2 concise sentences explaining the dish.
    **Ingredients:** Provide a short bullet list of the main ingredients only.
    **Nutrition (per serving):** Provide realistic estimates for:
    - Calories:
    - Carbohydrates:
    - Fat:
    - Protein:
    **Recipe Videos:**
    - **English Recipe:** https://www.youtube.com/results?search_query=${foodItem} recipe english
    - **Malayalam Recipe:** https://www.youtube.com/results?search_query=${foodItem} recipe malayalam
    Replace {food item} with the exact food name provided by the user.
    Ensure spacing and formatting are clean and consistent.
  `;

  try {
    const response = await ai.generateContent({
      model: MODEL_NAME,
      contents: `Provide information for: ${foodItem}`,
      generationConfig: {
        temperature: 0.7,
      },
      systemInstruction,
    });

    return response.response.text() || "No response received from the assistant.";
  } catch (error) {
    console.error("Gemini API Error:", error);
    throw new Error("Failed to fetch food information. Please try again.");
  }
}