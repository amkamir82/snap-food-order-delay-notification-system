import dataclasses


@dataclasses.dataclass
class DelayServiceData:
    name: str
    order_id: int


@dataclasses.dataclass
class AgentServiceData:
    agent_id: int
