from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    """Abstract base class for different notification channels."""
    
    @abstractmethod
    def send(self, user_id: str, message: str) -> None:
        pass

class EmailChannel(NotificationChannel):
    """Email notification channel implementation."""
    
    def send(self, user_id: str, message: str) -> None:
        # Implement email sending logic here
        pass

class InAppMessageChannel(NotificationChannel):
    """In-app messaging channel implementation."""
    
    def send(self, user_id: str, message: str) -> None:
        # Implement in-app message sending logic here
        pass

class NotificationService:
    """Central service for handling notifications across multiple channels."""
    
    def __init__(self):
        self.channels = [EmailChannel(), InAppMessageChannel()]
        
    def send_notification(self, user_id: str, recommendation_type: str) -> None:
        """Send a notification to the user based on recommendation type."""
        message = f"Recommended upgrade: {recommendation_type}"
        for channel in self.channels:
            try:
                channel.send(user_id, message)
                break  # Only use first successful channel
            except Exception as e:
                logging.error(f"Failed to send via {channel.__class__.__name__}: {str(e)}")