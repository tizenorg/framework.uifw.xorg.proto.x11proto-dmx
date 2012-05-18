
Name:       xorg-x11-proto-dmxproto
Summary:    X.Org X11 Protocol dmxproto
Version:    2.3
Release:    1.5
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/dmxproto-%{version}.tar.gz
Provides:   dmxproto
BuildRequires: pkgconfig(xorg-macros)

%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 




%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/dmx.h
%{_includedir}/X11/extensions/dmxproto.h
%{_datadir}/pkgconfig/dmxproto.pc


