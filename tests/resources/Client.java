package tests.resources;
// import jakarta.persistence.Entity;
// import jakarta.persistence.Id;
// import java.time.LocalDate;

@Entity
@Table(name="customer")
public class Client {
    @Id
    private Long id;

}