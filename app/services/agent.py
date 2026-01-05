class AgentService:
    """
    Cœur logique de l'agent Relation Client IA
    (IA branchée plus tard)
    """

    def handle_message(self, message: str, client_id: str | None = None) -> str:
        return (
            f"Message reçu : '{message}'. "
            "Un agent vous répondra sous peu."
        )
