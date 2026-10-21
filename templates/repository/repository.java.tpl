package ${package};

import ${entity_package}.${entity};
import ${repository_import};
import org.springframework.stereotype.Repository;

@Repository
public interface ${entity}Repository
        extends ${repository_type}<${entity}, ${id_type}> {

}