class ChatAgent:
    """
    Agent IA minimal (logique métier).
    La connexion à OpenAI viendra ensuite.
    """

    def reply(self, message: str, client_id: str | None = None) -> str:
        # Logique simple pour l’instant
        return (
            f"[Agent IA] J'ai bien reçu votre message : '{message}'. "
            "Un conseiller virtuel va analyser votre demande."
        )
