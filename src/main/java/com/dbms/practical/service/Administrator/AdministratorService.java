package com.dbms.practical.service.Administrator;

import com.dbms.practical.entity.Administrator;
import com.dbms.practical.repository.AdministratorRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class AdministratorService implements IAdministrator {

    private final AdministratorRepository administratorRepository;

    @Override
    public Administrator getAdministrator(String username, String password) {

        Administrator administrator = administratorRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("Administrator not found!"));

        if (verifyPassword(administrator, password)) {

            Administrator output = new Administrator();

            output.setId(administrator.getId());
            output.setName(administrator.getName());
            output.setSurname(administrator.getSurname());

            return output;
        }

        throw new RuntimeException("Invalid password!");
    }

    private boolean verifyPassword(Administrator administrator, String password) {
        return administrator.getPassword().equals(password);
    }
}