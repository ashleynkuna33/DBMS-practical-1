package com.dbms.practical.service.User;

import com.dbms.practical.entity.User;
import com.dbms.practical.dto.UserUpdateRequest;

public interface IUser {
    // a user can only login and update their password

    User getUser(String studentNumber, String password); //for login (student sends their student number and password only
    User updateUser(Long id, UserUpdateRequest request); // pass the user and request

}
