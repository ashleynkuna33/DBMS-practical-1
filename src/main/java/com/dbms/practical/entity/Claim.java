package com.dbms.practical.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.util.Date;

@NoArgsConstructor
@AllArgsConstructor
@Entity
@Getter
@Setter
@Table(name = "claim")
public class Claim {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long claim_id;

    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @ManyToOne
    @JoinColumn(name = "item_id", nullable = false)
    private Item item;

    @ManyToOne
    @JoinColumn(name = "admin_id", nullable = true)
    private Administrator admin;

    @CreationTimestamp
    @Column(name="created_at", nullable=false, updatable=false)
    private Date created_at;

    @UpdateTimestamp
    @Column(name = "updated_at", nullable=false)
    private Date updated_at;

    @Enumerated(EnumType.STRING)
    private Status status;

    public enum Status {
        SUBMITTED,
        UNDER_REVIEW,
        APPROVED,
        REJECTED
    }

    private String feedback;
    
}
