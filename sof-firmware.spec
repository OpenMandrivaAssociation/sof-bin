%undefine _debugsource_packages
%global _firmwaredir %{_prefix}/lib/firmware

Name:           sof-firmware
Summary:        Firmware Data Files for SOF Drivers
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        2024.03
Release:        1
URL:            https://github.com/thesofproject/sof-bin
Source:         https://github.com/thesofproject/sof-bin/releases/download/v%{version}/sof-bin-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:	rsync

%description
Various firmware data files for SOF drivers.

%prep
%autosetup -p1 -n sof-bin-%{version}

%build

%install
mkdir -p "%{buildroot}%{_firmwaredir}/intel" "%{buildroot}%{_bindir}"
FW_DEST="%{buildroot}%{_firmwaredir}/intel" TOOLS_DEST="%{buildroot}%{_bindir}" ./install.sh
%fdupes -s %{buildroot}

%files
%license LICENCE.*
%doc README.*
%{_bindir}/*
%{_firmwaredir}/*
