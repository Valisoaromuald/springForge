from config.package_mapping import PACKAGE_MAPPING

class PackageResolver:

    def resolve(
        self,
        source_package: str,
        target: str
    ) -> str:

        if target not in PACKAGE_MAPPING:
            raise ValueError(
                f"Unknown target package: {target}"
            )

        current_package = source_package.rsplit(".", 1)[-1]
        if current_package not in ("model", "entity"):
            raise ValueError(
                f"Cannot resolve package from '{source_package}'"
            )

        return source_package.rsplit(".", 1)[0] + "." + PACKAGE_MAPPING[target]