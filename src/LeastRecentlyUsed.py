from collections import deque

def lru(page_references, frame_size):
    page_faults = 0
    page_hits = 0
    frames = set()
    page_queue = deque()

    for page in page_references:
        if page not in frames:
            page_faults += 1
            if len(frames) == frame_size:
                removed_page = page_queue.popleft()
                frames.remove(removed_page)
            frames.add(page)
            page_queue.append(page)
        else:
            page_hits += 1
            page_queue.remove(page)
            page_queue.append(page)

    return page_faults, page_hits

page_references = [] # Add page
frame_size = 3

page_faults, page_hits = lru(page_references, frame_size)

print("Page Faults:", page_faults)
print("Page Hits:", page_hits)