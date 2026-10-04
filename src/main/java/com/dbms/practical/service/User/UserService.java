package com.dbms.practical.service.User;

import com.dbms.practical.dto.UserUpdateRequest;
import com.dbms.practical.entity.User;
import com.dbms.practical.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class UserService implements IUser {

    private final UserRepository userRepository;

    @Override
    public User getUser(String username, String password) {

        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found!"));

        if (verifyPassword(user, password)) {

            User output = new User();

            output.setId(user.getId());
            output.setStudentNumber(user.getStudentNumber());

            return output;
        }

        throw new RuntimeException("Invalid password!");
    }

    private boolean verifyPassword(User user, String password) {
        return user.getPassword().equals(password);
    }

    @Override
    public User updateUser(Long id, UserUpdateRequest request) {

        User user = userRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("User not found!"));

        handleUpdate(user, request);

        return userRepository.save(user);
    }

    private void handleUpdate(User user, UserUpdateRequest request) {

        if (request.getStudentNumber() != null) {
            user.setStudentNumber(request.getStudentNumber());
        }

        if (request.getPassword() != null) {
            user.setPassword(request.getPassword());
        }
    }
}