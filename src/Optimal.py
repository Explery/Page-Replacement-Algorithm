def opt(page_references, frame_size):
    page_frames = []
    page_faults = 0
    page_hits = 0

    for page in page_references:
        if page not in page_frames:
            if len(page_frames) < frame_size:
                page_frames.append(page)
            else:
                print()
            page_faults += 1
        else:
            page_hits += 1


page_references = [] # Add page
frame_size = 3

page_faults, page_hits = opt(page_references, frame_size)

print("Page Faults:", page_faults)
print("Page Hits:", page_hits)