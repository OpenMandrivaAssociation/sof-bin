%global _firmwaredir %{_prefix}/lib/firmware

Name:           sof-firmware
Summary:        Firmware Data Files for SOF Drivers
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        2023.09
Release:        1
URL:            https://github.com/thesofproject/sof-bin
Source:         https://github.com/thesofproject/sof-bin/releases/download/v%{version}/sof-bin-%{version}.tar.gz
BuildArch:      noarch
  
BuildRequires:  fdupes

%description
Various firmware data files for SOF drivers.

%prep
%setup -q -n sof-bin-%{version}

%build

%install
mkdir -p %{buildroot}%{_firmwaredir}/intel
mkdir -p %{buildroot}%{_bindir}
FW_DEST=%{buildroot}%{_firmwaredir}/intel \
TOOLS_DEST=%{buildroot}%{_bindir} \
./install.sh
rm -rf %{buildroot}%{_bindir}
%fdupes -s %{buildroot}

# workaround for changing symlinked directory
%pre
if [ -L %{_firmwaredir}/intel/sof-tplg ]; then
  f=$(readlink -f %{_firmwaredir}/intel/sof-tplg)
  case $f in
    %{_firmwaredir}/intel/*)
      rm -rf $f
      rm -f %{_firmwaredir}/intel/sof-tplg;;
  esac
fi

%files
%license LICENCE.*
%doc README.*
%{_firmwaredir}/*
