
Name:       xorg-x11-proto-dmxproto
Summary:    X.Org X11 Protocol dmxproto
Version:    2.3
Release:    1.5
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-dmxproto.manifest 
Provides:   dmxproto
BuildRequires: pkgconfig(xorg-macros)

%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 




%files
%manifest xorg-x11-proto-dmxproto.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/dmx.h
%{_includedir}/X11/extensions/dmxproto.h
%{_datadir}/pkgconfig/dmxproto.pc


