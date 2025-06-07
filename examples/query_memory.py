#!/usr/bin/env python3
"""
Example: Query memory
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from memvid import MemvidRetriever
from memvid.config import get_default_config, get_codec_parameters
import time


def print_search_results(results):
    """Pretty print search results"""
    print("\nSearch Results:")
    print("-" * 50)
    for i, result in enumerate(results):
        print(f"\n[{i+1}] Text: {result}")


def main():
    print("Memvid Example: Query Memory")
    print("=" * 50)
    
    # Get video file type from codec parameters
    config = get_default_config()
    codec = config.get("codec", "h264")
    codec_params = get_codec_parameters(codec)
    video_file_type = codec_params.get("video_file_type", "mkv")
    
    # Check if memory files exist
    video_file = f"output/memory.{video_file_type}"
    index_file = "output/memory_index.json"
    
    if not os.path.exists(video_file) or not os.path.exists(index_file):
        print("\nError: Memory files not found!")
        print("Please run 'python examples/build_memory.py' first to create the memory.")
        return
    
    # Initialize retriever
    print(f"\nLoading memory from: {video_file}")
    retriever = MemvidRetriever(video_file, index_file)
    
    # Get stats
    stats = retriever.get_stats()
    print(f"\nMemory loaded successfully!")
    print(f"  Total chunks: {stats['index_stats']['total_chunks']}")
    
    # Example query
    query = "What are the latest developments in quantum computing?"
    print(f"\nSearching for: '{query}'")
    
    start_time = time.time()
    results = retriever.search(query, top_k=5)
    elapsed = time.time() - start_time
    
    print(f"Search completed in {elapsed:.3f} seconds")
    print_search_results(results)


if __name__ == "__main__":
    main()