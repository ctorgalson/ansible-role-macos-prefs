# Ansible Role macOS Prefs

This role sets macOS app preferences using version-controlled `plist` files.

## Requirements

No special requirements beyond macOS.

## Role Variables

| Name                    | Default value       | Description |
|-------------------------|---------------------|-------------|
| `prefs_prefs_directory` | `files/preferences` | The location for the role to discover plist files to upload and import as preferences. |

## Dependencies

No dependencies.

## Example Playbook

    - hosts: all
      roles:
        - role: ansible-role-macos-prefs

## License

GPLv3

## Author Information

Christopher Torgalson
