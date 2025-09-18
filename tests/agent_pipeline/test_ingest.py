from __future__ import annotations

from agent_pipeline.stages.ingest import load_documents


def test_load_documents_filters_invalid_entries() -> None:
    payload = {
        "scraped_documents": [
            {"url": "https://example.com/a", "markdown": "# Title", "metadata": {"mimeType": "text/markdown"}},
            {"url": "", "markdown": "# Missing URL"},
            "not-a-dict",
        ],
        "follow_up_documents": [
            {"url": "https://example.com/b", "content": "Notebook"},
        ],
    }

    docs = load_documents(payload)

    assert len(docs) == 2
    assert docs[0].doc_id == 1
    assert docs[1].doc_id == 2
    assert docs[0].metadata["mimeType"] == "text/markdown"
