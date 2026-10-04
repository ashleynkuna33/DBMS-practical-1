package com.dbms.practical.service.Item;

import com.dbms.practical.entity.Item;
import com.dbms.practical.dto.ItemRequest;

public interface IItem {
    // someone can report an item, change details, and remove it
    Item getItem(Long id);
    Item createItem(ItemRequest request);
    Item updateItem(Long id, Long user_id, ItemRequest request); // check if the user was the one who created the item at the first place
}
