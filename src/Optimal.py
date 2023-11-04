def optimal_page_replacement(pages, capacity):
    # Store the sequence of pages in a list
    page_sequence = list(pages)
    
    # To keep track of current pages in memory
    memory_state = []
    
    # To keep track of page faults
    page_faults = 0
    
    # To keep track of the time when a page is referenced
    time_since_last_used = {}
    
    for i, page in enumerate(page_sequence):
        if page not in memory_state:
            # Page Fault
            page_faults += 1
            
            # If there is still room in the memory
            if len(memory_state) < capacity:
                memory_state.append(page)
            else:
                # Choose the page to replace
                for m_page in memory_state:
                    if m_page not in page_sequence[i+1:]:
                        # If the page is not going to be used again, remove it
                        memory_state.remove(m_page)
                        break
                    else:
                        # If the page will be used in the future, mark when it will be used next
                        time_since_last_used[m_page] = page_sequence[i+1:].index(m_page)
                
                # Replace the page that is not going to be used for the longest time
                if len(time_since_last_used) != 0:
                    page_to_replace = max(time_since_last_used, key=time_since_last_used.get)
                    memory_state[memory_state.index(page_to_replace)] = page
                    # Clear the last used time
                    time_since_last_used.clear()
        else:
            # No page fault, so just update the order of pages in memory
            memory_state.remove(page)
            memory_state.append(page)
            
        # For visual representation, not part of the core algorithm
        print(f"Step {i+1}: Page {page}")
        print(f"Memory State: {memory_state}")
        print(f"Page Faults: {page_faults}\n")
        
    return page_faults

# Example usage:
pages = "7 2 3 1 2 5 3 4 6 7 7 1 0 5 4 6 2 3 0 1"
page_sequence = pages.split()
frame_capacity = 3
faults = optimal_page_replacement(page_sequence, frame_capacity)
print(f"Total Page Faults: {faults}")