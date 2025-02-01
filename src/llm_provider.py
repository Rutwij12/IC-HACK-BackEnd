from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
import os
import time
import asyncio
from typing import List, Tuple, Optional, Any

class LLMWrapper:
    def __init__(self, model: str = "claude-3-sonnet-20240307"):
        self.use_mock = os.getenv("MOCK", "false").lower() == "true"
        if self.use_mock:
            self.llm = MockLLM()
        else:
            self.llm = ChatAnthropic(model=model)
    
    def invoke(self, messages: List[Tuple[str, str]], **kwargs) -> Any:
        return self.llm.invoke(messages, **kwargs)
    
    async def ainvoke(self, messages: List[Tuple[str, str]], **kwargs) -> Any:
        return await self.llm.ainvoke(messages, **kwargs)
    
    def with_structured_output(self, output_schema):
        if self.use_mock:
            return self.llm.with_structured_output(output_schema)
        return self.llm.with_structured_output(output_schema)

class MockLLM:
    def __init__(self, delay: float = 0.5):
        self.delay = delay
        self._structured_output = None
    
    def _get_default_value(self, field_type: Any) -> Any:
        # Handle basic types
        if field_type == str:
            return "mock_string"
        elif field_type == int:
            return 0
        elif field_type == float:
            return 0.0
        elif field_type == bool:
            return False
        elif field_type == list:
            return []
        elif field_type == dict:
            return {}
        
        # Handle Optional types
        if hasattr(field_type, "__origin__") and field_type.__origin__ is Optional:
            return None
        
        # Handle Lists with specific types
        if hasattr(field_type, "__origin__") and field_type.__origin__ is list:
            return []
        
        # If it's a Pydantic model, recursively create it
        if hasattr(field_type, "model_fields"):
            return self._create_mock_pydantic_instance(field_type)
        
        # Default fallback
        return None

    def _create_mock_pydantic_instance(self, model_class):
        mock_data = {}
        for field_name, field_info in model_class.model_fields.items():
            mock_data[field_name] = self._get_default_value(field_info.annotation)
        return model_class(**mock_data)

    def invoke(self, messages: List[Tuple[str, str]], **kwargs) -> Any:
        time.sleep(self.delay)  # Simulate API latency
        
        if self._structured_output:
            return self._create_mock_pydantic_instance(self._structured_output)
            
        return type('Response', (), {
            'content': """Here's a sample scene response
            The scene takes place at sunset, with golden rays filtering through tall windows.
            A melancholic piano melody plays softly in the background.
            Sarah, with her distinctive auburn hair, sits at an antique desk."""
        })
    
    def with_structured_output(self, output_schema):
        self._structured_output = output_schema
        return self

    async def ainvoke(self, messages: List[Tuple[str, str]], **kwargs) -> Any:
        await asyncio.sleep(self.delay)  # Simulate API latency
        
        if self._structured_output:
            return self._create_mock_pydantic_instance(self._structured_output)
            
        return type('Response', (), {
            'content': """Here's a sample scene response
            The scene takes place at sunset, with golden rays filtering through tall windows.
            A melancholic piano melody plays softly in the background.
            Sarah, with her distinctive auburn hair, sits at an antique desk."""
        })

if __name__ == "__main__":
    # First load env variables
    load_dotenv(override=True)