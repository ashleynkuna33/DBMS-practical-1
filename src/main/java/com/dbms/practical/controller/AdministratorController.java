package com.dbms.practical.controller;

import com.dbms.practical.entity.Administrator;
import com.dbms.practical.service.Administrator.IAdministrator;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/administrators")
@AllArgsConstructor
public class AdministratorController {

    private final IAdministrator administratorService;

    @PostMapping("/login")
    public Administrator getAdministrator(
            @RequestParam String username,
            @RequestParam String password ) {

        return administratorService.getAdministrator(username, password);
    }

}
