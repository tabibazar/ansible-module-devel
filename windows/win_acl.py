#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2014, Phil Schwartz <schwartzmx@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_acl
version_added: ""
short_description: Set file/directory permissions for a system user or group.
description:
     - Add or remove rights/permissions for a given user or group for the specified src file or folder.
options:
  src:
    description:
      - File or Directory
    required: yes
    default: none
    aliases: []
  user:
    description:
      - User or Group to add specified rights to act on src file/folder
    required: yes
    default: none
    aliases: []
  state:
    description:
      - Specify whether to add (present) or remove (absent) the specified access rule
    required: no
    choices:
      - present
      - absent
    default: present
    aliases: []
  type:
    description:
      - Specify whether to allow or deny the rights specified
    required: yes
    choices:
      - allow
      - deny
    default: none
    aliases: []
  rights:
    description:
      - The rights/permissions that are to be allowed/denyed for the specified user or group for the given src file or directory.  Can be entered as a comma separated list (Ex. "Modify, Delete, ExecuteFile").  For more information on the choices see MSDN FileSystemRights Enumeration.
    required: yes
    choices:
      - AppendData
      - ChangePermissions
      - Delete
      - DeleteSubdirectoriesAndFiles
      - ExecuteFile
      - FullControl
      - ListDirectory
      - Modify
      - Read
      - ReadAndExecute
      - ReadAttributes
      - ReadData
      - ReadExtendedAttributes
      - ReadPermissions
      - Synchronize
      - TakeOwnership
      - Traverse
      - Write
      - WriteAttributes
      - WriteData
      - WriteExtendedAttributes
    default: none
    aliases: []
  inherit:
    description:
      - Inherit flags on the ACL rules.  Can be specified as a comma separated list (Ex. "ContainerInherit, ObjectInherit").  For more information on the choices see MSDN InheritanceFlags Enumeration.
    required: no
    choices:
      - ContainerInherit
      - ObjectInherit
      - None
    default: For Leaf File: None; For Directory: ContainerInherit, ObjectInherit;
    aliases: []
  propagation:
    description:
      - Propagation flag on the ACL rules.  For more information on the choices see MSDN PropagationFlags Enumeration.
    required: no
    choices:
      - None
      - NoPropagateInherit
      - InheritOnly
    default: "None"
    aliases: []
author: Phil Schwartz
'''

EXAMPLES = '''
# Restrict write,execute access to User Fed-Phil
$ ansible -i hosts -m win_acl -a "user=Fed-Phil src=C:\Important\Executable.exe type=deny rights='ExecuteFile,Write'" all

# Playbook example
# Add access rule to allow IIS_IUSRS FullControl to MySite
---
- name: Add IIS_IUSRS allow rights
  win_acl:
    src: 'C:\inetpub\wwwroot\MySite'
    user: 'IIS_IUSRS'
    rights: 'FullControl'
    type: 'allow'
    state: 'present'
    inherit: 'ContainerInherit, ObjectInherit'
    propagation: 'None'

# Remove previously added rule for IIS_IUSRS
- name: Remove FullControl AccessRule for IIS_IUSRS
    src: 'C:\inetpub\wwwroot\MySite'
    user: 'IIS_IUSRS'
    rights: 'FullControl'
    type: 'allow'
    state: 'absent'
    inherit: 'ContainerInherit, ObjectInherit'
    propagation: 'None'

# Deny Intern
- name: Deny Deny
    src: 'C:\Administrator\Documents'
    user: 'Intern'
    rights: 'Read,Write,Modify,FullControl,Delete'
    type: 'deny'
    state: 'present'
'''