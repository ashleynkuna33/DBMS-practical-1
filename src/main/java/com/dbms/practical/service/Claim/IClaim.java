package com.dbms.practical.service.Claim;

import com.dbms.practical.entity.Claim;
import com.dbms.practical.dto.ClaimRequest;

public interface IClaim {
    // a student can create a claim only (upload all the required documents and answer questions)
    // admin can review the claim STATUS: submitted -> review after admin opening
    // admin can write a feedback and/or move the status stage
    Claim createClaim(Long user_id, ClaimRequest request);
    Claim getClaim(Long user_id, Long id); // check if a student is viewing only their claims
    Claim getClaims(Long user_id); // return all claims made by the student

    Claim updateClaim(Long admin_id, ClaimRequest request); // only admin can modify the feedback and status
}
