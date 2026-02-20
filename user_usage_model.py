from dataclasses import dataclass

@dataclass
class UserUsageModel:
    """Data model representing a user's usage patterns and behavior."""
    
    user_id: str
    login_frequency: Dict[str, int]  # Maps dates to login counts
    feature_usage: Dict[str, int]     # Maps feature IDs to usage counts
    api_calls: Dict[str, int]        # Maps API endpoints to call counts
    last_login: datetime.datetime
    revenue_generated: float