package com.dbms.practical.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.util.Date;
import java.util.List;

@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "Item")
public class Item {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long item_id;

    private String title;
    private String category;
    private String description;

    @Enumerated(EnumType.STRING)
    @Column(nullable=false)
    private Status status;

    public enum Status {
        LOST,
        FOUND,
        CLAIMED,
        RETURNED
    }

    @ManyToOne
    @JoinColumn(name = "location_id")
    private  Location location;

    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @OneToMany(mappedBy = "item")
    private List<Claim> claims;

    @ManyToOne(fetch = FetchType.EAGER, cascade = CascadeType.ALL)
    private Administrator admin;

    @CreationTimestamp
    @Column(name = "created_at", updatable = false)
    private Date created_at;

    @UpdateTimestamp
    @Column(name = "updated_at")
    private Date updated_at;
}
