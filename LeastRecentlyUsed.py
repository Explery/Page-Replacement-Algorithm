from collections import deque

def lru(page_reference_string, frame_count):
    page_faults = 0
    page_hits = 0
    frames = set()
    page_queue = deque()

    for page in page_reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) == frame_count:
                removed_page = page_queue.popleft()
                frames.remove(removed_page)
            frames.add(page)
            page_queue.append(page)
        else:
            page_hits += 1
            page_queue.remove(page)
            page_queue.append(page)

    return page_faults, page_hits

page_reference_string = [] # Add page
frame_count = 3

page_faults, page_hits = lru(page_reference_string, frame_count)

print("Page Faults:", page_faults)
print("Page Hits:", page_hits)