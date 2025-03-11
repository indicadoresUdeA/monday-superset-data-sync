


def get_query_for_board_elements(dataframe, board_id): 

    main_string = "query { boards(ids:" +  board_id + ") { items_page(limit: 500) { items { id name"
    final_string = "} } } }"

    for index in len(dataframe["column_names"]):
        main_string = main_string + str(dataframe["column_names"][index]) + ": column_values(ids: \"" +  str(dataframe["column_ids"][index]) + "\") { text }" 

    return main_string