%undefine _debugsource_packages
%global _firmwaredir %{_prefix}/lib/firmware

Name:           sof-bin
Summary:        Files for working with SOF firmware
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        2025.01.1
Release:        1
URL:            https://github.com/thesofproject/sof-bin
Source:         https://github.com/thesofproject/sof-bin/releases/download/v%{version}/sof-bin-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:	rsync
Requires:	sof-firmware = %{EVRD}

%description
Files for working with SOF firmware

%package -n sof-firmware
Summary:	Various firmware data files for SOF drivers.
Group:		Hardware/Other
BuildArch:	noarch

%description -n sof-firmware
Various firmware data files for SOF drivers.

%prep
%autosetup -p1 -n sof-bin-%{version}

%build

%install
mkdir -p "%{buildroot}%{_firmwaredir}/intel" "%{buildroot}%{_bindir}"
FW_DEST="%{buildroot}%{_firmwaredir}/intel" TOOLS_DEST="%{buildroot}%{_bindir}" ./install.sh
%fdupes -s %{buildroot}

# In sof-firmware 2.2.6 (2024-05-11, OM 5.0),
# /usr/lib/firmware/intel/sof-tplg
# was a symlink. Now it's a directory. This scriptlet can go as soon as
# we stop supporting updates from anything that had <= 2.2.6
%pretrans -n sof-firmware -p <lua>
st = posix.stat("%{_firmwaredir}/intel/sof-tplg")
if st and st.type == "link" then
	os.remove("%{_firmwaredir}/intel/sof-tplg")
end

%files
%license LICENCE.*
%doc README.*
%{_bindir}/*

%files -n sof-firmware
%{_firmwaredir}/*
