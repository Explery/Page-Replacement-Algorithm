def optimal_page_replacement(pages, capacity):
    # List of current pages in memory
    memory = []
    # Page fault count
    page_faults = 0
    # Keep track of the usage of pages
    page_usage_dict = {}

    for i in range(len(pages)):
        # Find out when each page will be used next
        for j in range(i, len(pages)):
            if pages[j] in memory:
                page_usage_dict[pages[j]] = j
            else:
                page_usage_dict[pages[j]] = float('inf')

        # If the page is not present in memory
        if pages[i] not in memory:
            # If there is still room in the memory
            if len(memory) < capacity:
                memory.append(pages[i])
            else:
                # Find the page that will not be used for the longest time in the future
                furthest_used_page = max(memory, key=lambda page: page_usage_dict[page])
                # Replace that page with the new page
                memory[memory.index(furthest_used_page)] = pages[i]
            # Increment page faults
            page_faults += 1

        # After processing, remove the page from the usage dictionary if it won't be used again
        page_usage_dict.pop(pages[i], None)

        # For debug: Print the current memory state
        print(f"Step {i}: {memory}")

    return page_faults

# Example usage
pages = []
capacity = 3
print(f"Total page faults using Optimal Page Replacement: {optimal_page_replacement(pages, capacity)}")