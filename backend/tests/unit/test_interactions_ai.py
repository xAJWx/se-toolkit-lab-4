"""AI-generated unit tests for interactions - edge cases and boundary values."""

import pytest
from app.models.interaction import InteractionLogCreate, InteractionModel
from app.routers.interactions import _filter_by_item_id
from test_interactions import _make_log


class TestAIGenerated:
    """AI-generated edge case tests."""

    def test_filter_with_zero_item_id(self):
        """Test filtering with item_id=0 (boundary value)."""
        interactions = [
            _make_log(1, 1, 0),
            _make_log(2, 2, 1),
            _make_log(3, 3, 0),
        ]
        filtered = _filter_by_item_id(interactions, 0)
        assert len(filtered) == 2
        assert all(i.item_id == 0 for i in filtered)

    def test_create_with_empty_string_kind(self):
        """Test that empty string kind is accepted (boundary value)."""
        interaction = InteractionLogCreate(learner_id=1, item_id=1, kind="")
        assert interaction.kind == ""
