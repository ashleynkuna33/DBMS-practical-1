package com.dbms.practical.service.Administrator;

import com.dbms.practical.entity.Administrator;

public interface IAdministrator {
    //admin people can only be allowed to login only (access for new people will be explicitly be granted by the department )
    Administrator getAdministrator(String username, String password);
}
