package com.dbms.practical.controller;

import com.dbms.practical.dto.UserUpdateRequest;
import com.dbms.practical.entity.User;
import com.dbms.practical.service.User.IUser;
import lombok.*;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/users")
@AllArgsConstructor
public class UserController {

    private final IUser userService;

    @PostMapping("/login")
    public User getUser(
            @RequestParam String username,
            @RequestParam String password ) {

        return userService.getUser(username, password);
    }

    @PutMapping("/{id}")
    public User updateUser(
            @PathVariable Long id,
            @RequestBody UserUpdateRequest request ) {
        return userService.updateUser(id, request);
    }
}
